package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity8 extends AppCompatActivity {
    TextView tv;
    Button btn0;
    Button btn1;
    Button btn2;
    Button btn3;
    Button btn4;
    Button btn5;
    Button btn6;
    Button btn7;
    Button btn8;
    Button btn9;
    MyOnClickListener myOnClickListener;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main8);

        tv = findViewById(R.id.tv);
        btn0 = findViewById(R.id.btn0);
        btn1 = findViewById(R.id.btn1);
        btn2 = findViewById(R.id.btn2);
        btn3 = findViewById(R.id.btn3);
        btn4 = findViewById(R.id.btn4);
        btn5 = findViewById(R.id.btn5);
        btn6 = findViewById(R.id.btn6);
        btn7 = findViewById(R.id.btn7);
        btn8 = findViewById(R.id.btn8);
        btn9 = findViewById(R.id.btn9);
        myOnClickListener = new MyOnClickListener(tv);

//        btn0.setOnClickListener(myOnClickListener);
//        btn1.setOnClickListener(myOnClickListener);
//        btn2.setOnClickListener(myOnClickListener);
//        btn3.setOnClickListener(myOnClickListener);
//        btn4.setOnClickListener(myOnClickListener);
//        btn5.setOnClickListener(myOnClickListener);
//        btn6.setOnClickListener(myOnClickListener);
//        btn7.setOnClickListener(myOnClickListener);
//        btn8.setOnClickListener(myOnClickListener);
//        btn9.setOnClickListener(myOnClickListener);
        for (int i = 0; i < 10; i++) {
            Button button = findViewById(getResources().getIdentifier("btn" + i, "id", getPackageName()));
            button.setOnClickListener(myOnClickListener);
        }

        Button call = findViewById(R.id.btn_call);
        call.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });

    }

    public void myclick(){
        String txt = tv.getText()+"";
        Toast toast = Toast.makeText(getApplicationContext(), "Calling..."+txt,Toast.LENGTH_SHORT);
        toast.show();
    }





}

