# Sample code to process command-line arguments.
# Supports short and long names.

# The following options and logic are completely arbitrary
# and only provided as an example. Replace with required functionality.
while [ "$1" != "" ]; do
  case "$1" in
    -r | --root) rootUserCmd="-u root"; shift ;;
    -e | --entrypoint) entrypointCmd=""; bashCmd=""; shift ;;
    -o | --official) IMAGE_NAME=$IMAGE_NAME-ubi; TARGET_REGISTRY=quay.io/mongodb; shift ;;
    *) print_usage;;
  esac
done

