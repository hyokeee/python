package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity5 extends AppCompatActivity {
    EditText mine;
    EditText com;
    EditText result;
    Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main5);

        mine = findViewById(R.id.et_mine);
        com = findViewById(R.id.et_com);
        result = findViewById(R.id.et_result);
        btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                playGame();
            }
        });

    }

    public void playGame(){
        String m = mine.getText().toString();
        String c = "";
        String res = "";
        double rnd = Math.random();
        if(rnd>0.5){
            c = "홀";
        } else{
            c = "짝";
        }

        if(c.equals(m)){
            res = "승리";
        }else{
            res = "패배";
        }
        com.setText(c);
        result.setText(res);
    }


}

