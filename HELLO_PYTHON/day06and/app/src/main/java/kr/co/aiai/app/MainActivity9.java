package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity9 extends AppCompatActivity {
    EditText et;
    Button btn;
    TextView tv;
    String com;
    String txt="";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main9);

        et = findViewById(R.id.et);
        btn = findViewById(R.id.btn);
        tv = findViewById(R.id.tv);

        com = getCom();

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });

    }
    public void myclick(){
        String mine = et.getText()+"";
        int strike = getStrike(mine,com);
        int ball = getBall(mine,com);
        String str_old = tv.getText()+"";
        String str_new = mine+"   "+strike+"S"+ball+"B"+"\n";
        tv.setText(str_new+str_old);
//        txt += mine+"\t"+strike+"S"+ball+"B"+"\t"+com+"\n";
//        tv.setText(txt);
        if(strike ==3){
            Toast toast = Toast.makeText(getApplicationContext(), mine+"정답입니다.",Toast.LENGTH_SHORT);
            toast.show();
        }
        et.setText("");



    }

    public int getStrike(String mine,String com){
        int strike = 0;
        String m1 = mine.substring(0,1);
        String m2 = mine.substring(1,2);
        String m3 = mine.substring(2,3);

        String c1 = com.substring(0,1);
        String c2 = com.substring(1,2);
        String c3 = com.substring(2,3);

        if(m1.equals(c1)) strike ++;
        if(m2.equals(c2)) strike ++;
        if(m3.equals(c3)) strike ++;

        return strike;
    }

    public int getBall(String mine,String com){
        int ball = 0;
        String m1 = mine.substring(0,1);
        String m2 = mine.substring(1,2);
        String m3 = mine.substring(2,3);

        String c1 = com.substring(0,1);
        String c2 = com.substring(1,2);
        String c3 = com.substring(2,3);

        if(m1.equals(c2)||m1.equals(c3)) ball++;
        if(m2.equals(c1)||m2.equals(c3)) ball++;
        if(m3.equals(c1)||m3.equals(c2)) ball++;

        return ball;

    }

    public String getCom(){
        String com = "";
        int ran[] = new int[9];
        for(int i = 1; i<=ran.length; i++){
            ran[i-1] = i;
        }
        for(int i = 0; i<=100; i++){
            int rnd = (int)(Math.random()*9);
            int temp = ran[0];
            ran[0] = ran[rnd];
            ran[rnd] = temp;
        }
        com = ran[0]+""+ran[1]+""+ran[2];
        return com;
    }
}

