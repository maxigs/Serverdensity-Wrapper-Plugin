# Wrapper Plugin for Serverdensity
# 
# calls a external script to get data
# 
class plugin1:
  def run(self):
    # call the actual script to get the data
    # TODO : make this line actually work, seems to crash the agent.py everytime so far
    r = subprocess.Popen(['/pathto/dummy.rb'], stdout=subprocess.PIPE, close_fds=True).communicate()[0]
    
    # parse the json into a dictionary
    # TODO : replace this with something less evil using json moule or minjson supplied with the agent
    data = eval(r)
    
    return data