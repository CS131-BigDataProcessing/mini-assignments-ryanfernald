I use conda for virtual environments, which you can use too if you have it installed, if not you can activate a virtual environment in any other way.

    conda create -n venv
    conda activate venv

To install the packages needed for the virtual environment: 

    pip install -r requirements.txt

To run the cron tasks script: 

    chmod +x setup_cron_tasks.sh    # to make sure setup_cron_tasks.sh script has execute permissions
    ./setup_cron_tasks.sh           # to run the script imediately
    crontab -l                      # to view the list of tasks