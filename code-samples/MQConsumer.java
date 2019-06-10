package mqTest.mqTest;
 
import javax.jms.Connection;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.Session;
import javax.jms.TextMessage;
 
import org.apache.activemq.ActiveMQConnectionFactory;
 
public class MQConsumer {
	// Create a connection factory.
	
	public static void main(String[] args) {
	final ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory("<SSL endpoint>:61617");
	
	// Pass the username and password.
	connectionFactory.setUserName("<Username>");
	connectionFactory.setPassword("<Password>");
 
	// Establish a connection for the consumer.
	try {
	final Connection consumerConnection = connectionFactory.createConnection();
	
	consumerConnection.start();
	
	// Create a session.
	final Session consumerSession = consumerConnection.createSession(false, Session.AUTO_ACKNOWLEDGE);
 
	// Create a queue named "MyQueue".
	final Destination consumerDestination = consumerSession.createQueue("MyQueue");
 
	// Create a message consumer from the session to the queue.
	final MessageConsumer consumer = consumerSession.createConsumer(consumerDestination);
	
	// Begin to wait for messages.
	final Message consumerMessage = consumer.receive(1000);
 
	// Receive the message when it arrives.
	final TextMessage consumerTextMessage = (TextMessage) consumerMessage;
	System.out.println("Message received: " + consumerTextMessage.getText());
	
	consumer.close();
	consumerSession.close();
	consumerConnection.close();
	//pooledConnectionFactory.stop();
	
	}
	catch(JMSException j) {}
	}
} 