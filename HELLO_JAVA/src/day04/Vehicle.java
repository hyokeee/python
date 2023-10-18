package day04;

public class Vehicle {
	int wheel_cnt = 2;
	
	public void flex() {
		wheel_cnt = 4;
	}
	
	public static void main(String[] args) {
		Vehicle v = new Vehicle();
		System.out.println(v.wheel_cnt);
		v.flex();
		System.out.println(v.wheel_cnt);
	}
}
