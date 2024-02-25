-- HEAD --

-- Description
description = [[
    This is an Nmap NSE script for detecting SSH services.
]]

-- Author
author = "Michael Roberts"

-- Documentation
-- for a little help https://chat.openai.com/share/f48a039f-9d8d-45ec-b895-1c8e10d85ce0 

-- Import necessary libraries
local shortport = require("shortport")


-- RULE --


-- Port rule definition
portrule = shortport.port_or_service({22}, {"ssh"}, "tcp", "open")

-- Function to check protocol
port_protocol = function(host, port)
    return port.protocol == "tcp"
end


-- ACTION --


-- Action function
action = function(host, port)
    return "SSH service detected on port " .. port.number
end

