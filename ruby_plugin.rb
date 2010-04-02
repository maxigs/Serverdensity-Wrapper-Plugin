#!/usr/bin/env ruby
require 'rubygems'
require 'json'

# generate some data
# replace this with whatever data you actually have
data = {'test' => 3}

# return the data as json for the wrapper to parse
puts data.to_json
