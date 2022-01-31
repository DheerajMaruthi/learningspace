# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure('2') do |config|
    config.vm.define 'learningspace', primary: true do |learningspace|
        # The most common configuration options are documented and commented below.
        # For a complete reference, please see the online documentation at
        # https://docs.vagrantup.com.

        # Every Vagrant development environment requires a box. You can search for
        # boxes at https://vagrantcloud.com/search.
        learningspace.vm.box = 'generic/rhel8'
        learningspace.vm.hostname = 'LEARNINGSPACE'

        # Disable automatic box update checking. If you disable this, then
        # boxes will only be checked for updates when the user runs
        # `vagrant box outdated`. This is not recommended.
        # config.vm.box_check_update = false

        # Create a forwarded port mapping which allows access to a specific port
        # within the machine from a port on the host machine. In the example below,
        # accessing "localhost:8080" will access port 80 on the guest machine.
        # NOTE: This will enable public access to the opened port
        # config.vm.network "forwarded_port", guest: 80, host: 8080

        # Create a forwarded port mapping which allows access to a specific port
        # within the machine from a port on the host machine and only allow access
        # via 127.0.0.1 to disable public access
        # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
        learningspace.vm.network 'forwarded_port', guest: 8075, host: 8075, host_ip: '127.0.0.1'
        # learningspace.vm.network 'forwarded_port', guest: 5432, host: 5432, host_ip: '127.0.0.1'
        # Create a private network, which allows host-only access to the machine
        # using a specific IP.
        # config.vm.network "private_network", ip: "192.168.33.10"

        # Create a public network, which generally matched to bridged network.
        # Bridged networks make the machine appear as another physical device on
        # your network.
        # config.vm.network "public_network"

        # Share an additional folder to the guest VM. The first argument is
        # the path on the host to the actual folder. The second argument is
        # the path on the guest to mount the folder. And the optional third
        # argument is a set of non-required options.
        # config.vm.synced_folder "/static/data", "/vagrant_data"
        learningspace.vm.synced_folder './', '/home/vagrant/workspace/learningspace'
        # Provider-specific configuration so you can fine-tune various
        # backing providers for Vagrant. These expose provider-specific options.
        # Example for VirtualBox:
        #
        learningspace.vm.provider 'virtualbox' do |vb|
            # Display the VirtualBox GUI when booting the machine
            # vb.gui = true
            # Customize the amount of memory on the VM:
            vb.memory = '1024'
            vb.cpus = 1
            vb.name = 'Learningspace'
        end
        #
        # View the documentation for the provider you are using for more
        # information on available options.

        # Enable provisioning with a shell script. Additional provisioners such as
        # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
        # documentation for more information about their specific syntax and use.
        learningspace.vm.provision 'shell', inline: <<-SHELL
            TEXT_RESET='\e[0m'
            TEXT_BLINK='\e[5m'
            TEXT_YELLOW='\e[0;33m'
            TEXT_BLUE='\e[34m'
            TEXT_RED_B='\e[1;31m'
            sudo ex +"%s@DPkg@//DPkg" -cwq /etc/apt/apt.conf.d/70debconf
            sudo dpkg-reconfigure debconf -f noninteractive -p critical

            echo -e "${TEXT_BLUE}Updating the System Packages${TEXT_RESET}"
            sudo apt-get update
            sudo apt-get upgrade -y
            sudo apt-get dist-upgrade -y
            echo -e "${TEXT_BLUE}Your System is updated.${TEXT_RESET}"

            echo -e "${TEXT_BLUE}Deleting unused Software Update Packages and clean-up disk space${TEXT_RESET}"
            sudo apt-get autoremove -y
            sudo apt-get autoclean -y
            sudo apt-get remove -y
            sudo apt-get clean -y
            echo -e "${TEXT_BLUE}Cleanup process done.${TEXT_RESET}"

            echo -e "${TEXT_BLUE}Setting up the Ubuntu Language...${TEXT_RESET}"
            sudo locale-gen en_GB.UTF-8
            echo -e "${TEXT_BLUE}Ubuntu Language generation complete.${TEXT_RESET}"

            sudo apt-get -y install gettext
            echo -e "${TEXT_BLUE}Get Text Installation complete for langugages.${TEXT_RESET}"

            echo -e "${TEXT_BLUE}Installing Python, SQLite and pip...${TEXT_RESET}"
            sudo apt-get install -y python3-dev sqlite python-pip libpq-dev
            echo -e "${TEXT_BLUE}Python, SQLite and pip instaltion complete.${TEXT_RESET}"

            echo -e "${TEXT_BLUE}Upgrading pip to the latest version.${TEXT_RESET}"
            sudo pip install --upgrade pip
            echo -e "${TEXT_BLUE}pip upgrade done.${TEXT_RESET}"

            echo -e "${TEXT_BLUE}Install and configure python virtualenvwrapper.${TEXT_RESET}"
            sudo pip install virtualenvwrapper
            echo -e "${TEXT_BLUE}Virtualenvwrapper configuration complete.${TEXT_RESET}"

            # Commands the need to run only once at the time of first provisioning must be placed here
            if ! grep -q VIRTUALENV_ALREADY_ADDED /home/vagrant/.bashrc; then
                echo "# VIRTUALENV_ALREADY_ADDED" >> /home/vagrant/.bashrc
                echo "WORKON_HOME=~/.virtualenvs" >> /home/vagrant/.bashrc
                echo "PROJECT_HOME=/vagrant" >> /home/vagrant/.bashrc
                echo "export LEARNINGSPACE_ENV='DEV'" >> /home/vagrant/.bashrc
                echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
                sed -i 's/#force_color_prompt=yes/force_color_prompt=yes/' /home/vagrant/.bashrc
                sudo sed -i 's/#force_color_prompt=yes/force_color_prompt=yes/' /root/.bashrc
            fi

            echo -e "${TEXT_BLUE}Updating the System Packages${TEXT_RESET}"
            sudo apt-get update
            sudo apt-get upgrade -y
            sudo apt-get dist-upgrade -y
            echo -e "${TEXT_BLUE}Your System is updated.${TEXT_RESET}"

            echo -e "${TEXT_BLUE}Deleting unused Software Update Packages and clean-up disk space${TEXT_RESET}"
            sudo apt-get autoremove -y
            sudo apt-get autoclean -y
            sudo apt-get remove -y
            sudo apt-get clean -y
            echo -e "${TEXT_BLUE}Cleanup process done.${TEXT_RESET}"

            echo -e "Installing the npm and npm less configuration"
            sudo apt-get install npm -y
            sudo npm install -g less -y
            echo -e " Installing is done"

            # Output success message
            echo -e "${TEXT_BLUE}\nYour machine has been provisioned${TEXT_RESET}"
            echo "---------------------------------"
            echo "${TEXT_YELLOW}Learningspace server is available on port 8051 ${TEXT_RESET}"
            echo "         (you have to use 127.0.0.1 as opposed to 'localhost')"
            echo "Head over to$TEXT_BLUE$TEXT_BLINK http://localhost:8051$TEXT_RESET to get started"
        SHELL
    end

end
