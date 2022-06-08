#!/usr/bin/env ruby
puts ARGV[0].scan(/[A-Z]{1,3}[a-z]{1,3}[\W]{1,}/).join
