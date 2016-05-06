/**
 * Created by kuochehung on 5/6/16.
 */
import org.jgroups.JChannel;
import org.jgroups.Message;
import org.jgroups.ReceiverAdapter;
import org.jgroups.View;
import org.jgroups.util.Util;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class SimpleChat extends ReceiverAdapter {
    JChannel mChannel;
    String user_name = System.getProperty("user.name", "n/a");
    final List<String> mStates = new LinkedList<String>();

    private void start() throws Exception {
        mChannel = new JChannel();
        mChannel.connect("MyCluster");
        mChannel.getState(null, 10000);
        eventLoop();
        mChannel.close();
    }

    private void eventLoop() {
        InputStreamReader inputR = new InputStreamReader(System.in);
        BufferedReader bufferR = new BufferedReader(inputR);

        while(true) {
            try {
                System.out.println("> ");
                System.out.flush();
                String line = bufferR.readLine().toLowerCase();

                if(line.startsWith("quit") || line.startsWith("exit")) {
                    bufferR.close();
                    inputR.close();
                    break;
                }

                line = "[" + user_name + "]" + line;
                Message msg = new Message(null, null, line);
                mChannel.send(msg);
            } catch(Exception e){
                System.out.println("error: " + e);
            } finally {

            }
        }
    }

    @Override
    public void viewAccepted(View view) {
        System.out.println("** view: " + view + " entered");
    }

    @Override
    public void receive(Message msg) {
        String line = msg.getSrc() + " says: " + msg.getObject();
        System.out.println(line);
        synchronized(mStates) {
            mStates.add(line);
        }
    }

    @Override
    public void setState(InputStream input) throws Exception {
        List<String> list;
        list = (List<String>) Util.objectFromStream(new DataInputStream(input));
        synchronized (mStates) {
            mStates.clear();
            mStates.addAll(list);

            System.out.println(list.size() + " messages in chat history");
            for(String msg: list) {
                System.out.println(msg);
            }
        }
    }

    public static void main(String[] args) {
        SimpleChat chat = new SimpleChat();
        try {
            chat.start();
        } catch (Exception e) {
            System.out.println("error: " + e);
        } finally {

        }
    }
}
