#!/ffp/bin/perl

# V.0.1 Last modified: 2016.02.02
    # This script pings google.com with only one package in every 6 seconds.
    # The exit code and the formatted timestamp is saved in a specified logfile.
    # The script runs until explicitely killed.
    # to get the current date, the script uses the system date command.

use warnings;
use strict;
#use DateTime; # On the NAS the DateTime package was not installed, so the system date command was used.

# Output file is read from the command line parameter:
die "The output file has to be specified!\n" unless $ARGV[0];
my $filename = $ARGV[0];

# Output file is initialized. Header row is saved:
open (my $OUT, ">", $filename);
print $OUT "DateTime\tPing_exit_code\n";

while (1){ # The script will be running until it is killed.

    #my $dt = DateTime->now();
    my $ping_out = `busybox ping -c1 google.com`;
    my $exit_code = $?;
    my $time = `date +"%Y-%m-%d_%H:%M:%S"`;
    chomp $time;

    printf $OUT "%s\t%s\n", $time, $exit_code; #$dt->strftime("%Y-%m-%d_%H:%M:%S"), $?;

    sleep 6;
}

