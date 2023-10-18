package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity8Sem extends AppCompatActivity {
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

        btn0.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn1.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn2.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn3.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn4.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn5.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn6.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn7.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn8.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });
        btn9.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick(view); } });

        Button btn_call = findViewById(R.id.btn_call);

        btn_call.setOnClickListener(new View.OnClickListener() { public void onClick(View view) { myclick2();} });



    }

    public void myclick(View v){
        Button imsi = (Button) v;
        String str_old = tv.getText().toString();
        String str_new = imsi.getText().toString();
        tv.setText(str_old+str_new);
    }

    public void myclick2(){
        String txt = tv.getText()+"";
        Toast toast = Toast.makeText(getApplicationContext(), "Calling..."+txt,Toast.LENGTH_SHORT);
        toast.show();
    }


}

