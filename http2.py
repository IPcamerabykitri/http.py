
import pyshark

out_string=""
cap=pyshark.LiveCapture(interface='eth0',only_summaries="IP" "protocol")
cap.sniff(timeout=50)
for pkt in cap:
    out_file=open("date.txt","w")
    out_string += str(pkt)
    out_string += "\n"
    out_file.write(out_string)
cap.close()
