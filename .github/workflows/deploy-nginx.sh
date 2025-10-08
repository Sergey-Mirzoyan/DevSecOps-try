#!/bin/bash

RELEASE_NAME="nginx-local"
CHART_DIR="./nginx-simple"
IMAGE="nginx:latest"
REPORT_FILE="trivy-report.txt"

echo "=== Step 1: Deploy/Upgrade Helm release ==="
helm upgrade --install $RELEASE_NAME $CHART_DIR

echo "=== Step 2: Scan image with Trivy ==="
trivy image --format json $IMAGE > $REPORT_FILE

echo "=== Step 3: Check for Critical/High vulnerabilities ==="
CRITICAL_COUNT=$(jq '[.Results[].Vulnerabilities[] | select(.Severity=="CRITICAL" or .Severity=="HIGH")] | length' $REPORT_FILE)

if [ "$CRITICAL_COUNT" -gt 0 ]; then
  echo "❌ Found $CRITICAL_COUNT HIGH/CRITICAL vulnerabilities. Deployment stopped."
  exit 1
else
  echo "✅ No HIGH/CRITICAL vulnerabilities. Deployment safe."
fi

echo "=== Step 4: Forward NGINX metrics port ==="
kubectl port-forward svc/nginx-local-nginx-simple 9113:9113 &
PORT_FORWARD_PID=$!
sleep 3  # ждем пока порт откроется

echo "=== Step 5: Check NGINX metrics ==="
METRICS_URL="http://localhost:9113/metrics"
CONNECTIONS=$(curl -s $METRICS_URL | grep nginx_connections_total | awk '{print $2}')

if [ -z "$CONNECTIONS" ]; then
  echo "❌ NGINX metrics not available!"
else
  echo "✅ NGINX metrics available, total connections: $CONNECTIONS"
fi

kill $PORT_FORWARD_PID
echo "=== Step 6: Done ==="


