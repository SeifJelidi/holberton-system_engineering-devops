#!/usr/bin/env ruby
Ss = ARGV[0]
puts Ss.scan(/(?<=from:|to:|flags:)[^\]]*/).join","
