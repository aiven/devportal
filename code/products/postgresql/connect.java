import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class PostgresqlExample {
  public static void main(String[] args) throws ClassNotFoundException {
    final String HOST = // POSTGRESQL_HOST;
    final String PORT = // POSTGRESQL_PORT;
    final String DATABASE = // POSTGRESQL_DATABASE;
    final String USERNAME = // POSTGRESQL_USERNAME;
    final String PASSWORD = // POSTGRESQL_PASSWORD;

    Class.forName("org.postgresql.Driver");
    try (final Connection connection =
                 DriverManager.getConnection("jdbc:postgresql://" + HOST + ":" + PORT + "/" + DATABASE, USERNAME, PASSWORD);
         final Statement statement = connection.createStatement();
         final ResultSet resultSet = statement.executeQuery("SELECT version()")) {

      while (resultSet.next()) {
        System.out.println("Version: " + resultSet.getString("version"));
      }
    } catch (SQLException e) {
      System.out.println("Connection failure.");
      e.printStackTrace();
    }
  }
}
