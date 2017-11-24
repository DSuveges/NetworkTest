#!/usr/bin/env bash

# This script is written to test the accessibility of internet by pinging a remote host.
version="v.1.0"

# Get current date:
today=$(date +"%Y.%m.%d")

# Default variables:
targetURL="google.com"
outputFile="Network_test_${today}.tsv"
sleep_sec=5

# Store router IP address:
rooterIP=$(route -n | grep ^0 | awk '{print $2}')

# Help message:
function display_help {
    
    echo ""
    echo "${1}"
    echo ""
    echo "This script is written to test internet access by sending ping requests to a defined remote host."
    echo "Also, the script pings the rooter as well, to see if the lack in the internet service is due to rooter error."
    echo ""
    echo "Usage: ${0} -t google.com -s 10 -o OutputFilename"
    echo ""
    echo -e "\t-t: remote host, optional, google.com is the default."
    echo -e "\t-s: sleep time in sec between each ping requests, optional, 10s is the default."
    echo ""
    
    exit 1;
}

# Now these variables can be overriden by command line parameters:
OPTIND=1
while getopts ":ht:s:o:" optname; do
    case "$optname" in
        "t") targetURL=${OPTARG} ;;
        "r") rooterIP=${OPTARG} ;;
        "o") outputFile=${OPTARG} ;;
        "s") sleep_sec ;;
        "h") display_help ;;
        "?") display_help "[Error] Unknown option $OPTARG" ;;
        ":") display_help "[Error] No argument value for option $OPTARG";;
        *) display_help "[Error] Unknown error while processing options";;
    esac
done

# Write header:
(echo "# Version: ${version}"
echo "# Rooter IP: ${rooterIP}"
echo "# Target URL: ${targetURL}"
echo "# Output file name: ${outputFile}"
echo "# Sleep time: ${sleep_sec}"
echo -e "DateTime\tping_rooter\tping_remote") > "${outputFile}"

# now initialize an infinite loop:
while : ; do
    # ping remote:
    ping -c1 ${targetURL} > /dev/null
    targetCode="$?"
    
    # ping rooter:
    ping -c1 ${rooterIP} > /dev/null
    rooterCode="$?"
    
    # get date:
    timeStamp=$(date +"%Y-%m-%d_%H:%M:%S")
    
    # saving data:
    echo -e "${timeStamp:-NA}\t${rooterCode:-NA}\t${targetCode:-NA}" >> "${outputFile}"
    
    # Wait for the next ping:
    sleep ${sleep_sec}
done
