package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity9Sem extends AppCompatActivity {
    String com = "";
    EditText et;
    TextView tv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main9);

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
    public int getS(String mine,String com){
        int ret = 0;
        String m1 = mine.substring(0,1);
        String m2 = mine.substring(1,2);
        String m3 = mine.substring(2,3);

        String c1 = com.substring(0,1);
        String c2 = com.substring(1,2);
        String c3 = com.substring(2,3);

        if(m1.equals(c1)) ret++;
        if(m2.equals(c2)) ret++;
        if(m3.equals(c3)) ret++;

        return ret;
    }

    public void myclick(){
        String mine = et.getText()+"";
        int s = getS(mine,com);
    }

}

