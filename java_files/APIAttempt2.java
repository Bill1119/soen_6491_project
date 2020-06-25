package attempt1;

import java.util.List;

import org.eclipse.jgit.lib.Repository;
import org.refactoringminer.api.GitHistoryRefactoringMiner;
import org.refactoringminer.api.GitService;
import org.refactoringminer.api.Refactoring;
import org.refactoringminer.api.RefactoringHandler;
import org.refactoringminer.rm1.GitHistoryRefactoringMinerImpl;
import org.refactoringminer.util.GitServiceImpl;

public class APIAttempt2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		GitService gitService = new GitServiceImpl();
		GitHistoryRefactoringMiner miner = new GitHistoryRefactoringMinerImpl();

		Repository repo;
		try {
			repo = gitService.cloneIfNotExists(
					"/home/steve/Steve/git/commons-rng",
					"https://github.com/apache/commons-rng.git");
//			repo = gitService.cloneIfNotExists(
//					"tmp/refactoring-toy-example",
//					"https://github.com/danilofes/refactoring-toy-example.git");
			// For all with sample
			//			miner.detectAll(repo, "master", new RefactoringHandler() {
			//				  @Override
			//				  public void handle(String commitId, List<Refactoring> refactorings) {
			//				    System.out.println("Refactorings at " + commitId);
			//				    for (Refactoring ref : refactorings) {
			//				      System.out.println(ref.toString());
			////				      System.out.println(ref.toJSON());
			//				    }
			//				  }
			//				});
			// For between 2 commits with sample
			//			// start commit: 819b202bfb09d4142dece04d4039f1708735019b
			//			// end commit: d4bce13a443cf12da40a77c16c1e591f4f985b47
			//			miner.detectBetweenCommits(repo, 
			//					"819b202bfb09d4142dece04d4039f1708735019b", "d4bce13a443cf12da40a77c16c1e591f4f985b47",
			//					new RefactoringHandler() {
			//				@Override
			//				public void handle(String commitId, List<Refactoring> refactorings) {
			//					System.out.println("Refactorings at " + commitId);
			//					for (Refactoring ref : refactorings) {
			//						//			      System.out.println(ref.toString());
			//						System.out.println(ref.toJSON());
			//					}
			//				}
			//			});
			
			// start commit: 40fd7ad244b350d657ca4f1a9efe667c52697327
			// end commit: 3ca48892811538e911eb3c5bafd60b4d9ca92483
			miner.detectBetweenCommits(repo, 
					"40fd7ad244b350d657ca4f1a9efe667c52697327", "3ca48892811538e911eb3c5bafd60b4d9ca92483",
					new RefactoringHandler() {
				@Override
				public void handle(String commitId, List<Refactoring> refactorings) {
					System.out.println("Refactorings at " + commitId);
					for (Refactoring ref : refactorings) {
//						System.out.println(ref.toString());
						System.out.println(ref.toJSON());
					}
				}
			});
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
