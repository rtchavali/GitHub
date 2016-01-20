#
# Cookbook Name:: apache
# Recipe:: default
#
# Copyright 2016, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute


#install apache
package "apache2" do
 action :install
end

#start apache service
#make sure to service starts on reboot
service "apache2" do
	action [ :enable, :start ]
end


#write our home page

cookbook_file "/var/www/index.html" do
	source "index.html"
	mode "0644"
end
