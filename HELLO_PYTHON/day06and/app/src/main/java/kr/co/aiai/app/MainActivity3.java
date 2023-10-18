package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity3 extends AppCompatActivity {
    EditText et1;
    EditText et2;
    EditText et3;
    Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        et1 = findViewById(R.id.et1);
        et2 = findViewById(R.id.et2);
        et3 = findViewById(R.id.et3);
        btn = findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                sumNumber();
            }
        });

    }

    public void sumNumber(){
        int a = Integer.parseInt(et1.getText()+"");
        int b = Integer.parseInt(et2.getText()+"");
        int sum= 0;
        for(int i = a; i<=b; i++){
            sum += i;
        }
        et3.setText(sum+"");
    }

}

