#!/bin/bash

# Название релиза и chart
RELEASE_NAME="nginx-local"
CHART_DIR="./nginx-simple"

# Имя образа для проверки
IMAGE="nginx:latest"

# Файл отчёта Trivy
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

echo "=== Step 4: Done ==="

