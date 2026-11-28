#!/usr/bin/env bash

set -euo pipefail

echo "======================================"
echo " Banking Project - Terraform Plan"
echo "======================================"

# Locate Terraform project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TERRAFORM_DIR="$(dirname "$SCRIPT_DIR")"

cd "$TERRAFORM_DIR"

# Initialize Terraform
echo ""
echo "[1/2] Initializing Terraform..."
terraform.exe init -input=false

# Generate Terraform plan
echo ""
echo "[2/2] Generating Terraform execution plan..."

terraform.exe plan \
    -var-file="environments/dev/terraform.tfvars" \
    -out="banking-dev.tfplan"

echo ""
echo "======================================"
echo " Terraform plan generated successfully!"
echo "======================================"
