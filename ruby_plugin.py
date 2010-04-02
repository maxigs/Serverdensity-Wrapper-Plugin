# Ruby Script Wrapper Serverdensity Plugin
# 
# Tries to execute a ruby script with a similar filename as the current one and parses its JSON return data along to the agent.
# 
# USAGE:
# - Rename this file to match the naming conventions for your custom plugin
# - Rename the class of this plugin to match the filename
# - Create a ruby file which can be directly executed and returns JSON data following the
#   The ruby file needs to have a similar filename as this file (but with .rb ending)
# - Put this file along with your ruby script into the Serverdensity plugin folder
# - Dont forget to make the rb-file executable
# - Restart the agent and enjoy your ruby plugin
# 
# For further infos on Serverdensity plugins see: http://www.serverdensity.com/docs/agent/plugins/
# 
import os, logging, subprocess
class ruby_plugin:
  def run(self):
    current_dir     = os.path.split(__file__)[0]
    current_name    = os.path.split(__file__)[1].replace('.py', '')
    
    pluginLogger    = logging.getLogger('plugin:' + current_name)
    
    script_filename = current_name + '.rb'
    script_path     = os.path.join(current_dir, script_filename)
    
    if os.path.exists(script_path):
      pluginLogger.debug('found "' + script_filename + '"')
      
      try:
        r = subprocess.Popen([script_path], stdout=subprocess.PIPE, close_fds=True).communicate()[0]
        data = eval(r) # TODO : replace me with proper and secure parsing
        pluginLogger.debug('external data pulled successfully')
        return data
      
      except:
        pluginLogger.error('unable to pull external data')
        return False
      
    else:
      pluginLogger.error('could not found "' + script_filename + '", skipping')
      return False
