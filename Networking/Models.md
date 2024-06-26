## OSI model

| Layer Name | Protocol | Protocol Data Unit | Addressing | Explanation |
|------------|----------|--------------------|------------|-------------|
| Application | HTTP, FTP, IRC, SSH, DNS etc...| Messages | n/a | End user layer
| Presentation | SSL, SSH, IMAP, FTP, MPEG, JPEG | | |  Syntax layer
| Session | ApI's, Sockets, WinSock | | | Synch & send to port
| Transport | TCP, UDP | Segment | Port#'s | Sorts out which client and server programs are supposed to get that data. End-to-end connection.
| Network | IP, ICMP, IPSec, IGMP | Packet/Diagram | IP Address | Allows different networks to communicate with each other through devices known as routers
| Data Link | Ethernet, PPP, Switch, Bridge | Frames | MAC Address | Responsible for defining a common way of interpreting these signals so network devices can communicate
| Physical | n/a | Bits | n/a | Physical devices that interconnect computers (Coax, fiber, wireless, hubs, repeaters)
___
## TCP/IP five layer model

| Layer Name | Protocol | Protocol Data Unit | Addressing | Explanation |
|------------|----------|--------------------|------------|-------------|
| Application | HTTP,SMTP etc...| Messages | 7,6,5 OSI layers | 
| Transport | TCP/UDP | Segment | Port#'s | Sorts out which client and server programs are supposed to get that data. End-to-end connection
| Network | IP | Packet/Datagram | IP Address | Allows different networks to communicate with each other through devices known as routers
| Data Link | Ethernet, Wi-Fi | Frames | MAC Address | Responsible for defining a common way of interpreting these signals so network devices can communicate
| Physical | n/a | Bits | n/a | Physical devices that interconnect computers
___
## TCP/IP 

| Layer Name | OSI model layers|
|------------|----------|
| Application | 7,6,5
| Host to Host | 4
| Internet | 3
| Network Access | 2,1

`Etherent`: Ethernet standards also define a protocol responsible for getting data 
to nodes on the same network or link  
`Internetwork`: A collection of networks connected together throughout routers (Internet)

![img.png](img/img.png)

The physical layer is the delivery truck and the roads. The data link layer is 
how the delivery trucks get from one intersection to the next over and over. 
The network layer identifies which roads need to be taken to get from address A to address B. 
The transport layer ensures that delivery driver knows how to knock on your door 
to tell you your package has arrived. 
And the application layer is the contents of the package itself.
___
## Unicast, Multicast, Broadcast
`Unicast`: one device transmits data to another device.  
A unicast transmission is always meant for just one receiving address. 
At the ethernet level this is done by looking at a special bit in the destination MAC address. 
If the least significant bit in the first octet of a destination address is set to zero, 
it means that ethernet frame is intended for only the destination address. 
This means it would be sent to all devices on the collision domain, but only actually received and processed by the intended destination.

`Multicast`: If the least significant bit in the first octet of a destination address is set to one, it means you're dealing with a multicast frame. 
A multicast frame is set to all devices on the local network segment. It will be accepted or discarded by each device depending on criteria 
aside from their own hardware MAC address. Network interfaces can be configured to accept 
lists of configured multicast addresses for these sorts of communications. 

`Broadcast`:  In ethernet, broadcast is sent to every single device on a LAN. 
This is accomplished by using a special destination known as a broadcast address. 
The ethernet broadcast address is all F's `FF:FF:FF:FF:FF:FF`. Ethernet broadcasts are used so that devices can learn more about each other.
___
## Encapsulation
`Encapsulation`:  
![img_4.png](img/img_4.png)

![img_16.png](img/img_16.png)

![img_17.png](img/img_17.png)

Application layer = in this case the actual website
Using Hypertext Transfer Protocol, HTTP because websites are written in HTML
The website can be quite large, so it has to be "broken up" into smaller chunks to be sent,
this is because some protocols like `Ethernet`, has a maximum amount of data that we can transfer for each frame that we send. 
For each chunk of data that we send across the network, we have a maximum amount of data that we can send in each one. 
The application layer, works in conjunction with the transport layer to take that data, break it into smaller pieces, and then add it to a header.

![img_19.png](img/img_18.png)

The transport layer, sets up a session between our client and our server, we need specific information in there to allow that to happen (like an envelope for a letter, here the "envelope" is called a `segment`). 
In this case, it's a source port, a destination port number, some flags, which is just some general information about what's happening in the transaction, a sequence number, 
an acknowledgement number, and those keep track of how much data has been sent and received. 

This information allows the client and the server to set up a session and keep track of what data has been sent and received. 

Now, that's just one component of this transaction. In order to know where we are sending this data, we need to tell it what the source and 
destination IP addresses are. 
So we need to know where on the internet or on a network the server and the client are. 
So we take our transport layer information, which is going to keep that session between our endpoints going, and then we send it down to the network layer, 
so we take our segment and it becomes the payload of our network layer.

![img_20.png](img/img_19.png)

and then we add this header, we add the source IP, destination IP, a value called the TTL, or time to live, 
which tells it how far this packet can travel at a maximum distance, 
and other information that we add into the network layer header to make this transaction work correctly. 

So now we have our segment inside the payload of our network layer header. This is called a `packet`. 
![img_20.png](img/img_20.png)

This particular one is an IP header, or Internet Protocol, specifically, Internet Protocol version 4. So our network layer header is going to allow us to know what two endpoints on 
the internet, or any network, we're going to send this information to. 

Now in order to get our packet to go from one device to the next, from our workstation to the switch, from the switch to the router, from the router to the 
cable modem, from the cable modem out to the internet, and all the hops that go along the internet, we're going to need a `data link layer` header here. 
So we send our network layer packet down to the data link layer, and we put it in a `frame`. 

![img_21.png](img/img_21.png)

![img_22.png](img/img_22.png)

Now a frame is just a chunk of data with a `data link layer header`. In this particular case, this is an Ethernet header, so this is going to be an `Ethernet frame`, 
and we'll send data from our workstation to the switch, from the switch to our router, from a router to the cable modem. 
However, once we get to the cable modem, we're going to use a different protocol there which requires 
a different frame. So what we'll end up doing is taking the packet out of the frame and putting it into a new frame, 
and this happens consistently throughout the transaction as removing the data across the internet.

The packet will remain the same; the `frame header` will change as it goes from segment to segment to segment. 
Now in our frame, especially an Ethernet frame,  there's a maximum amount of data that we can send.
So here, our data is still intact, that chunk of website that we're sending is still encapsulated inside of this frame. 
There's also a `transport layer header`, there's a `network layer header`, and then we have this `Ethernet header`. 
When we're working with this, especially Ethernet, the data part of this can have something called a `maximum transmission unit` for Ethernet, or `MTU`, 
and for Ethernet that's typically 1500 bytes. 

Once we have our frame constructed with the source MAC address, destination MAC address, and then layer 3 protocol that we're using, 
we can then take that frame, send it down to the physical layer. 

![img_23.png](img/img_23.png)

When we send it down to the physical layer, what's going to happen here is we're going to convert that into 1s and 0s, and then the 1s and 0s are converted into a signal. That signal could be a light signal 
that we send across fiber optics, it could be an electrical pulse that we send across a copper wire, or it might be an electromagnetic signal that we send with wireless.

![img_24.png](img/img_24.png)

So in order  get the website over to our workstation, we have to send all that data up and down the OSI model in order to make all the hops that we need to make in order to get it from our server over to our workstation.
And that involves taking our application layer information, putting it inside a segment, taking the segment, putting it inside a packet, taking the packet, putting it inside of a frame, and then sending it across the wire.
___
## Sources
- Ross Bagurdes, Network Concepts and Protocols, https://app.pluralsight.com/
- Google, The Bits and Bytes of Computer Networking, https://www.coursera.org/



