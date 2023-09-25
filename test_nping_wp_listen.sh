#!/bin/bash

check_wp_site() {
    local domain=$1
    echo -n "Checking $domain... "
    
    # Check if the domain is listening on port 80 (HTTP)
    ncat -z -w 1 $domain 80 # __________________________________________________________
    http_result=$?

    if [ $http_result -eq 0 ]; then
        echo "Port 80 is listening"
        exit 1 #There is a problem here, it quites the whole program  __________________________________________________________
    else
        echo "Port 80 is not listening"
        exit 1
    fi

    # Print the domain name
    echo "Domain: $domain"

    # Check and print the results
    if [ $http_result -eq 0 ]; then
        echo "Port 80: ok"
    else
        echo "Port 80: failure"
        exit 1
    fi

    if [ $https_result -eq 0 ]; then
        echo "Port 443: ok"
    else
        echo "Port 443: failure"
        exit 1
    fi
}

# input data for script
source data.sh

# create loop to test all sub-domains

# test
domains=" a01-stud-01.ToddBooth.com a01-stud-02.ToddBooth.com a01-stud-03.ToddBooth.com a01-stud-04.ToddBooth.com a01-stud-05.ToddBooth.com a01-stud-06.ToddBooth.com a01-stud-07.ToddBooth.com a01-stud-08.ToddBooth.com a01-stud-09.ToddBooth.com a01-stud-10.ToddBooth.com a01-stud-11.ToddBooth.com a01-stud-12.ToddBooth.com"

for domain in $domains; do
    check_wp_site $domain
done

