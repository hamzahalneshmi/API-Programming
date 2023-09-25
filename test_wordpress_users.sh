#!/bin/bash

# Get list of Wordpress usernames
# requires WP_USERNAME and WP_KEY environment variables

echo "WP_USERNAME: $WP_USERNAME"
echo "WP_KEY: $WP_KEY"
echo 'response=$(curl -X GET -u "${WP_USERNAME}:${WP_KEY}" ${BASE_URL}/users)'

# PROTOCOL="http"
PROTOCOL="https"
BASE_URL="$PROTOCOL://toddbooth.com/wp-json/wp/v2"
response=$(curl -X GET -u "${WP_USERNAME}:${WP_KEY}" ${BASE_URL}/users)

# Check if the following user name exists
TEST_NAME="d7001dhamaln3" #There is a problem here __________________________________________________________

echo "checking for $TEST_NAME"

# echo $response

# Process JSON items without pipes
items=$(jq -c '.[]' <<< "$response")

# Split items into an array
IFS=$'\n' read -rd '' -a items_array <<< "$items"

# Loop through the items
for item in "${items_array[@]}"; do
    name=$(jq -r '.name' <<< "$item")
    # echo "$name"
    if [ "$name" = "$TEST_NAME" ]; then
        echo "name exists: $name"
        exit 0
    fi
done
echo "name does not exist: $TEST_NAME"
exit 1
