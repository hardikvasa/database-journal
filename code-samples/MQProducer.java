package mqTest.mqTest;
 
import javax.jms.Connection;
import javax.jms.DeliveryMode;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.MessageProducer;
import javax.jms.Session;
import javax.jms.TextMessage;
 
import org.apache.activemq.ActiveMQConnectionFactory;
import org.apache.activemq.jms.pool.PooledConnectionFactory;
 
public class MQProducer {
	public static void main(String[] args) {
        System.out.println("Begin.."); // Display the string.
        // Create a connection factory.
        // Create a connection factory.
        final ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory("<SSL endpoint>:61617");
 
        // Pass the username and password.
        connectionFactory.setUserName("<UserName>");
        connectionFactory.setPassword("<Password>");
 
        // Create a pooled connection factory.
        final PooledConnectionFactory pooledConnectionFactory = new PooledConnectionFactory();
        pooledConnectionFactory.setConnectionFactory(connectionFactory);
        pooledConnectionFactory.setMaxConnections(10);
 
        // Establish a connection for the producer.
        try {
        		final Connection producerConnection = pooledConnectionFactory.createConnection();
        		producerConnection.start();
       
        
	        // Create a session.
	        final Session producerSession = producerConnection.createSession(false, Session.AUTO_ACKNOWLEDGE);
	
	        // Create a queue named "MyQueue".
	        final Destination producerDestination = producerSession.createQueue("MyQueue");
	
	        // Create a producer from the session to the queue.
	        final MessageProducer producer = producerSession.createProducer(producerDestination);
	        producer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
	        
	        // Create a message.
	        final String text = "TestMessage!";
	        TextMessage producerMessage = producerSession.createTextMessage(text);
	
	        // Send the message.
	        producer.send(producerMessage);
	        System.out.println("Message sent.");
	        
	        producer.close();
	        producerSession.close();
	        producerConnection.close();
        
        }
        catch (JMSException j) {}
	}
}