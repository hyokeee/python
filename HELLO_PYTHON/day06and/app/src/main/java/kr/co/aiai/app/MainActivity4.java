package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;
import java.util.Arrays;


public class MainActivity4 extends AppCompatActivity {
    EditText et1;
    EditText et2;
    EditText et3;
    EditText et4;
    EditText et5;
    EditText et6;
    Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);

        et1 = findViewById(R.id.et1);
        et2 = findViewById(R.id.et2);
        et3 = findViewById(R.id.et3);
        et4 = findViewById(R.id.et4);
        et5 = findViewById(R.id.et5);
        et6 = findViewById(R.id.et6);
        btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                makeLotto();
            }
        });
    }

    public void makeLotto(){

        int[] lotto = new int[45];
        for(int i = 1; i<=lotto.length; i++){
            lotto[i-1] = i;
        }

        for(int i = 0; i<=100; i++){
          int rnd = (int)(Math.random()*45);
            int temp = lotto[0];
            lotto[0] = lotto[rnd];
            lotto[rnd] = temp;
        }
        Arrays.sort(lotto,0,6);
        et1.setText(lotto[0]+"");
        et2.setText(lotto[1]+"");
        et3.setText(lotto[2]+"");
        et4.setText(lotto[3]+"");
        et5.setText(lotto[4]+"");
        et6.setText(lotto[5]+"");



    }




}

