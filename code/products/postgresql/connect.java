import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Locale;

public class PostgresqlExample {
  public static void main(String[] args) throws ClassNotFoundException {
    String host, port, databaseName, userName, password;
    host = port = databaseName = userName = password = null;
    for (int i = 0; i < args.length - 1; i++) {
      switch (args[i].toLowerCase(Locale.ROOT)) {
        case "-host": host = args[++i]; break;
        case "-username": userName = args[++i]; break;
        case "-password": password = args[++i]; break;
        case "-database": databaseName = args[++i]; break;
        case "-port": port = args[++i]; break;
      }
    }
    // JDBC allows to have nullable username and password
    if (host == null || port == null || databaseName == null) {
      System.out.println("Host, port, database information is required");
      return;
    }
    Class.forName("org.postgresql.Driver");
    try (final Connection connection =
                 DriverManager.getConnection("jdbc:postgresql://" + host + ":" + port + "/" + databaseName + "?sslmode=require", userName, password);
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
