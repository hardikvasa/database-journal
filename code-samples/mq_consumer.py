#Consumer
import time
import stomp
import logging
import ssl

class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, message):
        print('MyListener:\nreceived a message "{}"\n'.format(message))
        global read_messages
        read_messages.append({'id': headers['message-id'], 'subscription':headers['subscription']})


class MyStatsListener(stomp.StatsListener):
    def on_disconnected(self):
        super(MyStatsListener, self).on_disconnected()
        print('MyStatsListener:\n{}\n'.format(self))

read_messages = []
hosts = [('<host>', '61614')]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('my_listener', MyListener())
conn.set_listener('stats_listener', MyStatsListener())
conn.set_ssl(for_hosts=hosts, ssl_version=ssl.PEM_HEADER)
conn.start()
conn.connect('<userName>', '<password>', wait=True)

conn.subscribe(destination='/queue/test', id=3, ack='client-individual')
time.sleep(30)

#read messages
for message in read_messages:
    conn.ack(message['id'], message['subscription'])
conn.disconnect()
