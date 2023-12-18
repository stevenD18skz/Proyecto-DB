-- Crear la función generar_valor_cliente
CREATE OR REPLACE FUNCTION generar_valor_cliente()
RETURNS TRIGGER AS $$
BEGIN
  NEW.usuario := upper(substring(NEW.nombre from 1 for 2)) || nextval('sec_cliente') || upper(substring(NEW.apellido from 1 for 1)) || '-' || substring(NEW.num_celular from 1 for 5);
  NEW.pass_word := NEW.usuario;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;



-- Crear el trigger cliente_trigger
CREATE TRIGGER cliente_trigger
BEFORE INSERT ON CLIENTE
FOR EACH ROW
EXECUTE FUNCTION generar_valor_cliente();



CREATE OR REPLACE FUNCTION verificar_correo() RETURNS TRIGGER AS $$
BEGIN
  IF NEW.email NOT LIKE '%@gmail.com' THEN
    RAISE EXCEPTION 'El correo debe terminar con @gmail.com';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER correo_trigger
BEFORE INSERT OR UPDATE ON CLIENTE
FOR EACH ROW EXECUTE PROCEDURE verificar_correo();



-- Crear la función generar_valor
CREATE OR REPLACE FUNCTION generar_valor()
RETURNS TRIGGER AS $$
BEGIN
  NEW.id_trabajador := upper(substring(NEW.nombre from 1 for 2)) || nextval('sec_trabajador') || upper(substring(NEW.apellido from 1 for 1)) || '-' || substring(NEW.documento from 1 for 3);
  NEW.pass_word := NEW.id_trabajador;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;



-- Crear el trigger trabajador_trigger
CREATE TRIGGER trabajador_trigger
BEFORE INSERT ON TRABAJADOR
FOR EACH ROW
EXECUTE FUNCTION generar_valor();



CREATE OR REPLACE FUNCTION calculate_distance(cliente_nombre text, trabajador_nombre text)
RETURNS float AS $$
DECLARE
  lat1 float;
  lon1 float;
  lat2 float;
  lon2 float;
BEGIN
  SELECT 
    CAST(split_part(dir_gps, ',', 1) AS FLOAT), 
    CAST(split_part(dir_gps, ',', 2) AS FLOAT)
  INTO lat1, lon1
  FROM cliente
  WHERE usuario = cliente_nombre;

  SELECT 
    CAST(split_part(dir_gps, ',', 1) AS FLOAT), 
    CAST(split_part(dir_gps, ',', 2) AS FLOAT)
  INTO lat2, lon2
  FROM trabajador
  WHERE id_trabajador = trabajador_nombre;

  RETURN 1.60934 * 69.1 * sqrt((lat2 - lat1)^2 + (cos(lat1 / 57.3) * (lon2 - lon1))^2);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION calcular_promedio(_id VARCHAR)
RETURNS FLOAT AS $$
DECLARE
    promedio FLOAT;
BEGIN
    SELECT AVG(calificacion) INTO promedio
    FROM contrato
    WHERE id_trabajador = _id;

    RETURN promedio;
END; $$ LANGUAGE plpgsql;
