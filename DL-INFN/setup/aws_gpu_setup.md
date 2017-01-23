# Deep learning on AWS

This is a very brief guide to getting setup for deep learning with Tensorflow and Keras on an AWS GPU instance. It walks through setting up an instance from an AMI (Amazon Machine Image) that has Tensorflow installed already -- this is the hard part and it is already done. Most of this guide is about setting up IPython notebook so that you can conveniently experiment in your browser.

## Tensorflow AMI

The AMI is based on this AMI provided by Stanford: http://cs231n.github.io/aws-tutorial/

It has CUDA 7.5 and CuDNN 4.0 installed, along with Tensorflow 0.9, Keras 1.0.5, and all other dependencies for the notebooks already installed in an Anaconda python environment. After launching the instance, the environment can be activated by running

```bash
source activate tensorflow 
```

The AMI id is ami-97ba3a80.

## Sign up

First you need to sign up for AWS at https://aws.amazon.com/, enter payment information, etc. Don't worry, you will only pay for what you use.

## Launch instance

You can launch this AMI by going to https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-97ba3a80

This should give you a list of instance types to choose from. We want the g2.2xlarge GPU instance, so select it. After that, click the Next button at the bottom of the page to get to "Step 3: Configure Instance Details".

Here you can change your "Purchasing option". If you select "Request Spot instances", you can enter a bid price for the instance. This means that it may take longer for you to get the instance and the instance could be shutdown at an arbitrary time, but you can usually get an instance for much cheaper than the On Demand price of $0.65/hr. You should see the current Spot price for different regions after (the higher you max price, the faster you will get the instance and the more likely you are to retain the instance). I would recommend a Spot instance for simple experimentation and On Demand when you are sure you want to retain the instance for more serious work.

Clicking next again will get you to "4. Add Storage". Here you can choose to attach EBS volumes to the instance if you have any. Additionally, you can choose to retain the boot volume when the instance terminates by unchecking the "Delete on Termination" option. Note that retained volumes will be subject to EBS pricing.

After selected your Purchasing option, skip ahead to step "6. Configure Security Group" at the top of the screen. Here we will add 2 security rules (if you already have a security group defined, you can choose an existing security group instead).
1. Click "Add Rule" and select "HTTPS" as the Type
2. Click "Add Rule" again, check that Type is "Custom TCP Rule", enter 8888 as the port, and select "Anywhere" as the Source

Click "Review and Launch" at the bottom of the page. You can review your configuration, then click "Launch". A dialog will appear to create or select a key pair. If you need to, create a key pair and download the .pem file to a safe place on your computer.

After requesting the instance, you should see a view of the AWS console where you can see the status of your instance. After the instance is ready, we can log in!

## Logging into the instance

First, find your .pem file and restrict the permissions on it:
```
chmod 400 pem_file_name.pem
```

Get the Public DNS URL of your instance in the AWS console (mine was ec2-52-23-241-12.compute-1.amazonaws.com), and ssh to the host:

```
ssh -i pem_file_name.pem ubuntu@ec2-52-23-241-12.compute-1.amazonaws.com
```

## Install needed packages
```
sudo apt-get install h5py
sudo pip install keras
```
## Install and set up Jupyter

First, let's install Jupyter:
```
sudo pip install jupyter
```

In order to use our instance via IPython notebook, we need to create a self-signed SSL certificate so your browser can securely connect to IPython notebook on the instance. The following will start a wizard to create the certificate - answer the questions as well as you can.

```
mkdir certs && cd certs
sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
```

Let's also generate a password to use to log in. Start `ipython` and run
```python
from IPython.lib import passwd
passwd()
```

Copy and save the sha1 string that was generated for later and exit IPython. We need to configure IPython notebook. The following will create a `~/.jupyter/jupyter_notebook_config.py` file.
```
jupyter notebook --generate-config
```

Let's change the default config to use our new certificate and password:
```
cd ~/.jupyter/
nano jupyter_notebook_config.py
```

Put the following at the top of the file, substituting in the password sha1 and certificate path, and save the file.
```
c = get_config()

c.IPKernelApp.pylab = 'inline'

c.NotebookApp.certfile = u'/home/ubuntu/certs/mycert.pem' #location of your certificate file
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:68c136a5b064...'  #the encrypted password we generated above
c.NotebookApp.port = 8888
```

You can now start the IPython notebok by running `jupyter notebook`. You should now be able to navigate to https://<your-instance-public-dns>:8888 in your browser (don't forget the https://). You will likely get a warning that the certificate can't be verified. This is as expected, just proceed anyways. Then you will have an opportunity to enter your password for IPython notebook.

Much of the preceding setup came from http://blog.impiyush.me/2015/02/running-ipython-notebook-server-on-aws.html

## Install AWS CLI:

You can do almost everything you need on AWS on the commandline with the AWS CLI without having to do things with the AWS console page. For more information on installation and usage, refer to Lot of details at http://docs.aws.amazon.com/cli/latest/userguide/installing.html.
