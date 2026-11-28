
#!/usr/bin/env bash

set -euo pipefail

echo "======================================"
echo " Banking Project - Terraform Apply"
echo "======================================"

# Locate Terraform project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TERRAFORM_DIR="$(dirname "$SCRIPT_DIR")"

cd "$TERRAFORM_DIR"

# Check whether the saved plan exists
PLAN_FILE="banking-dev.tfplan"

if [[ ! -f "$PLAN_FILE" ]]; then
    echo "ERROR: Terraform plan file not found."
    echo "Run terraform_plan.sh first."
    exit 1
fi

# Apply the reviewed Terraform plan
echo ""
echo "Applying the saved Terraform plan..."

terraform.exe apply -input=false "$PLAN_FILE"

echo ""
echo "======================================"
echo " Terraform apply completed successfully!"
echo "======================================"
