package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity7 extends AppCompatActivity {
    EditText et_first;
    EditText et_last;
    TextView tv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main7);

        et_first = findViewById(R.id.et_first);
        et_last = findViewById(R.id.et_last);
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
        String a = et_first.getText()+"";
        int aa = Integer.parseInt(a);
        String b = et_last.getText().toString();
        int bb = Integer.parseInt(b);
        String txt = "";
        /*
        for (int i=aa; i<=bb; i++){
            for(int j=1; j<=i; j++){
                txt += "*";
            }
            txt += "\n";
        }
        tv.setText(txt);*/

        for(int i = aa; i<=bb; i++){
            txt += getStar(i);
        }
        tv.setText(txt);
    }

    public String getStar(int cnt){
        String res = "";
        for(int i = 0; i <cnt; i++){
            res += "*";
        }
        res += "\n";
        return res;
    }



}

