#!/bin/bash

# path to log_analysis_project directory
dir="$(pwd)"
cron_logs_dir="$dir/cron_logs"

# 1: Backup a folder daily at 5 AM and directs output to backup.log in cron_logs
backup_job="0 5 * * * tar -czf $dir/backup_folder.tar.gz /path/to/your/folder > $cron_logs_dir/backup.log 2>&1"

#2: Send a reminder email every Monday at 6 AM (assumes that you have mail setup) and and directs output to email.log file in cron_logs
email_job="0 6 * * 1 echo 'Reminder email' | mail -s 'Weekly Reminder' user@example.com > $cron_logs_dir/email.log 2>&1"

#3: Clear log files larger than 10MB in the logs directory every day at midnight and and directs output to filter_file_size.log file in cron_logs
clear_logs_job="0 0 * * * find $cron_lots_dir -type f -size +10M -exec rm {} \; > $cron_logs_dir/filter_file_size.log 2>&1"

# writing the cron jobs to the crontab
(crontab -l 2>/dev/null; echo "$backup_job") | crontab -
(crontab -l 2>/dev/null; echo "$email_job") | crontab -
(crontab -l 2>/dev/null; echo "$clear_logs_job") | crontab -
