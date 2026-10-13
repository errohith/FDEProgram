DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE rolname = 'fde_user'
   ) THEN
      CREATE USER fde_user WITH PASSWORD 'rohith143!';
   END IF;
END
$$;