package kr.co.aiai.app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final TextView text = findViewById(R.id.tv);
        Button btn = findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                String a = (String) text.getText();
                if(a.equals("Good Evening")){
                    text.setText("Good Morning");
                }else if(a.equals("Good Afternoon")){
                    text.setText("Good Evening");
                } else{
                    text.setText("Good Afternoon");
                }

            }

        });


    }

  /*  public void clickBtn(View v){
        TextView text = (TextView) findViewById(R.id.tv);
        String a = (String) text.getText();
        if(a.equals("Good Evening")){
            text.setText("Good Morning");
        }else if(a.equals("Good Afternoon")){
            text.setText("Good Evening");
        } else{
            text.setText("Good Afternoon");
        }


    }*/

}

