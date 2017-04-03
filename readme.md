## running yedit.py (edit nginx configuration for desired domain)
Run the following after populating `fields.conf` with your desired username and email.

```python yedit.py name-of-your-docker-compose-YAML.yml ```

(`test.yml` is the YAML file which should replace the `docker-compose.yml` in the [ssl-ized docker-ized cesium](https://github.com/brunston/docker-compose-cesium))

## running wsedit.py (edit running Cesium container to have proper websocket connections)
Run the following after identifying the path to `$cesium_web_folder/public/scripts/main.jsx`.

```python wsedit.py /path/to/cesium_web/public/scripts/main.jsx```


