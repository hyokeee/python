package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity6 extends AppCompatActivity {
    EditText et;
    TextView tv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main6);

        et = findViewById(R.id.et);
        tv = findViewById(R.id.tv);
        Button btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });

    }

    public void myclick(){
        String dan = et.getText()+"";
        int ddan = Integer.parseInt(dan);
        String text = "*****"+ddan+"단*****\n";
        for(int i=1; i<=9; i++){
            text += ddan + " * " + i + " = " + (ddan*i) + "\n";
        }
        tv.setText(text.toString());
    }




}

