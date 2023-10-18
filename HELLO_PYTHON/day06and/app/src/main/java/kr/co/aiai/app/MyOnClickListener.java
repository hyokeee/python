package kr.co.aiai.app;

import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MyOnClickListener implements View.OnClickListener{
    String txt ="";
    TextView tv;
    public MyOnClickListener(){}
    public MyOnClickListener(TextView tv){
        this.tv = tv;
    }
    @Override
    public void onClick(View view) {
        if (view instanceof Button) {
            Button button = (Button) view;
            String buttonText = button.getText().toString();
            txt += buttonText;
            tv.setText(getTxt());
        }

    }

    public String getTxt(){
        return txt;
    }
}
