# Giphy Integration Service for Mattermost
This integrations service is used to enable an external search engine ([Giphy](https://en.wikipedia.org/wiki/Giphy)) to be queried based on commands issued in a Mattermost channel using Mattermost [outgoing webhooks](https://github.com/mattermost/platform/blob/master/doc/integrations/webhooks/Outgoing-Webhooks.md).

Once installed, users can type `gif: keyword` to send a query to the Giphy search engine and return with a post containing one non-deterministic search result from the Giphy database of animated GIF files matching `keyword`. The animation will appear below in the posted message.

Powered by [Giphy](http://giphy.com/).

## Requirements
To run this integration you need:

1. A **web server** supporting Python 3.6.  Previous versions of this fork required 2.7.
2. A **[Mattermost account](http://www.mattermost.org/)** [where outgoing webhooks are enabled](https://github.com/mattermost/platform/blob/master/doc/integrations/webhooks/Outgoing-Webhooks.md#enabling-outgoing-webhooks)

Many web server options will work, below we provide instructions for [**Heroku**](HEROKU.md) and a general [**Linux/Ubuntu**](LINUX.md) server.

## Ubuntu Linux 18.04 Install
The following procedure shows how to install this project on a Linux web server running Ubuntu 18.04. The following instructions work behind a firewall so long as the web server has access to your Mattermost instances.

### Giphy integration service download and environment configuration
```bash
sudo apt install python3-pip python3-dev build-essential -y
sudo git clone https://github.com/dwaynepryce/mattermost-integration-giphy.git /opt/mattermost-integration-giphy
sudo chown -R mattermost:mattermost /opt/mattermost-integration-giphy
cd /opt/mattermost-integration-giphy
sudo su mattermost
python3 -m pip install virtualenv
python3 -m virtualenv -ppython3 venv
source venv/bin/activate
pip install -r requirements-frozen.txt
python setup.py install
```

### Mattermost configuration
1. Log in to your Mattermost account. Click the three dot menu at the top of the left-hand side and go to **Integrations** > **Slash Commands**
2. Under *Add a new command*, enter `gif` into **Command Trigger Word**
3. Paste your Web Server domain into *Callback URLs*, making sure to add `http://` to the beginning and `/new_post` to the end so it looks similar to `http://<your-web-server-domain>:<MATTERMOST_GIPHY_PORT>/new_post` and click **Add**
4. Select `POST` method
5. (optional) Choose a username and icon url (more details [here](https://docs.mattermost.com/developer/slash-commands.html#set-up-a-custom-command))
6. (optional) Check the autocomplete checkbox, add `[KEYWORD]` as the hint, `Returns a GIF from Giphy based on the keyword` as the description and `Get a GIF from Giphy` as the descriptive label
7. Copy the *Token* from your newly created slash command that appears under the *Existing commands* section


### Final Giphy integration service runtime configuration
Edit env.sh and put the *Token* from the Mattermost configuration in `MATTERMOST_GIPHY_TOKEN`.

```bash
sudo cp /opt/mattermost-integration-giphy/mattermost-integration-giphy.service /lib/systemd/system/mattermost-integration-giphy.service
sudo systemctl enable mattermost-integration-giphy.service
sudo systemctl start mattermost-integration-giphy.service
```

That's it! You should be able to type `gif: hello` or `/gif hello` into any channel and see a GIF from Giphy's translate service