import java.util.Scanner;

public abstract class Reflexao{
    private int dias;
    private String experiencia;
    private String desejo;


    public void execute(int dias, int experiencia, String desejo){
        this.dias = dias;
        this.experiencia = experiencia;
        this.desejo = desejo;
    }
   public void ask(String desejo, int experiencia){
       Scanner value = new Scanner(System.in);
       System.out.println("Me conte seu desejo");
       this.desejo = value.nextLine();
       System.out.println("Seu desejo foi:"+ this.desejo);
       Scanner value1 = new Scanner(System.in);
       System.out.println("Quantos meses de experiencia voce possui?");
       this.experiencia = value1.nextLine();
       System.out.println("Meses de experiência foram:"+ this.experiencia);
   }
   public void returns (int dias, int experiencia){
       if(experiencia==0){
           System.out.println("Oras, mas voce nem começou??");
        }
       if(experiencia<2){
           System.out.println("Ok..voce precisa estudar mais para aprimorar suas tecnicas!!!");
       }
       else if(experiencia>=6){
           System.out.println("Melhor! Acredito que agora seu conhecimento esteja em nível básico. Procure algumas certificações!");
        }
        else{
            System.out.println("Hora de buscar um estágio, não? Ou quer deixar o tempo de prática passar?");

        }}
    public void AplicarInsight(int experiencia){
        if(experiencia<2){
            System.out.println("Tá tudo errado. Primeiro, comece estudando linux e sistemas operacionais. Após isso, baixa um linux (VM) e seu PC. Agora, faça um curso de segurança, envolvendo segurança ética (hacking etc)");

        }

    }
    public void GetGrade(String dias, int experiencia){
        Scanner a = new Scanner(System.in);
        System.out.println("QUANTOS DIAS VOCE DESEJA ESTUDAR NA SEMANA?");
        this.dias = a.nextLine();
        System.out.println("VOCE DESEJA ESTUDAR EM TAIS DIAS:"+ this.dias);
        Scanner h = new Scanner(System.in);
        System.out.println("Quantos meses de experiencia voce adquiriu a mais?");
        this.experiencia = h.nextLine();
        System.out.println("Meses de experiência atualizados"+ this.experiencia);
    }
}
public class AdvancedReflexao extends Reflexao {
    private int numberOfHours;

    public void setNumberOfHours(int hours) {
        this.numberOfHours = hours;
    }

    public void studyPlan() {
        System.out.println("Criando plano de estudos " + dias + " tais dias " + numberOfHours + " e horas de estudo por dia.");
        System.out.println("Seu objetivo para aprimorar " + experiencia + " e meses de experiencia necessarios");
    }

    @Override
    public void AplicarInsight(int experiencia) {
        if (experiencia < 3) {
            System.out.println("Voce está pronto para aprofundar nesses tópicos!");
        } else {
            super.AplicarInsight(experiencia);
        }
    }
}

public class JornadaDoProjeto( String atualizar, int dias_estudados){

    public void hh(String atualizar, int dias_estudados){
        this.atualizar = atualizar;
        this.dias_estudados = dias_estudados;
    }
    public void Apresente_Jornada(String atualizar, int dias_estudados){
        Scanner a = new Scanner(System.in);
        System.out.println("ATUALIZE SEUS CONTEUDOS APRENDIDOS");
        this.atualizar = a.nextLine();
        System.out.println("CONTEUDOS ATUALIZADOS:"+ this.atualizar);
        Scanner b = new Scanner(System.in);
        System.out.println("QUANTOS DIAS VOCE JÁ ESTUDOU");
        this.dias_estudados = b.nextLine();
        System.out.println("DIAS DE ESTUDO ATUALIZADOS"+ this.dias_estudados);
}
