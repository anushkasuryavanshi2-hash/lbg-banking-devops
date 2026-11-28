
#!/usr/bin/env bash

set -euo pipefail

echo "======================================"
echo " Banking Project - Terraform Checks"
echo "======================================"

# Move to the Terraform project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TERRAFORM_DIR="$(dirname "$SCRIPT_DIR")"

cd "$TERRAFORM_DIR"

# Step 1: Check Terraform formatting
echo ""
echo "[1/3] Checking Terraform formatting..."
terraform.exe fmt -check -recursive
echo "Formatting check passed."

# Step 2: Initialize Terraform
echo ""
echo "[2/3] Initializing Terraform..."
terraform.exe init -input=false
echo "Terraform initialization completed."

# Step 3: Validate Terraform configuration
echo ""
echo "[3/3] Validating Terraform configuration..."
terraform.exe validate
echo "Terraform validation passed."

echo ""
echo "======================================"
echo " All Terraform checks passed!"
echo "======================================"
