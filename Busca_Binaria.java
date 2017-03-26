
public class Busca_Binaria {
	
	
	public static void main(String args[]){
		
		int[] vetor = {1,2,3,4,50,6,7,8,9,10};
		
		int result = binary_search(vetor,50,0,vetor.length-1);
		System.out.println(result);
	}
	
	public static int binary_search(int[] vetor,int x, int esq, int dir){
		//int esq=0;
		//int dir = vetor.length-1;
		
		int meio = (int) Math.ceil((esq+dir)/2);
		
		if(esq==dir && vetor[meio]!=x)
			return -1;
		
		if(x<vetor[meio])
			return binary_search(vetor,x, esq,meio);
		else if (x>vetor[meio])
			return binary_search(vetor,x,meio+1,vetor.length-1);
		else
			return meio;
	}
	
	
}
