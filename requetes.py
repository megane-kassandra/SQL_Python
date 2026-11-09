def print_aeroport(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT  a.nom as nom_aeroport, a.ville FROM Aeroports a ORDER BY a.ville")
    rows = cursor.fetchall()
    return rows

def print_vols(conn, statut):
    cursor = conn.cursor()
    cursor.execute("SELECT v.numero_vol, v.date_vol, v.statut FROM Vols v WHERE v.statut = ?", (statut,))
    rows = cursor.fetchall()
    return rows

def get_id_vol(conn, numero_vol):
   cursor = conn.cursor()
   cursor.execute("SELECT v.id_vol FROM Vols v WHERE v.numero_vol = ?", (numero_vol,))
   row = cursor.fetchone()
   if row is None:
       return f"Vol introuvable"
   else:
        return row
    
def print_passagers(conn, id_vol):
    cursor = conn.cursor()
    cursor.execute("SELECT p.nom as nom_passager , p.prenom as prenom_passager FROM Passagers p WHERE p.id_vol = ?", (id_vol,))
    rows = cursor.fetchall()
    return rows

def print_passager_num_vol(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT p.nom as nom_passager, p.prenom as prenom_passager, v.numero_vol FROM Passagers p INNER JOIN Vols v ON v.id_vol = p.id_vol")
    rows = cursor.fetchall()
    return rows

def print_num_vol_ville_depart_ville_arrivee(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT v.numero_vol, a1.ville as ville_depart, a2.ville as ville_arrivee  FROM Vols v INNER JOIN Aeroports a1 ON v.id_depart = a1.id_aeroport INNER JOIN Aeroports a2 ON v.id_arrivee = a2.id_aeroport")
    rows = cursor.fetchall()
    return rows

def print_passager_vol(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT p.nom as nom_passager , p.prenom as prenom_passager FROM Passagers p INNER JOIN Vols v ON p.id_vol = v.id_vol WHERE v.numero_vol = \"CM101\" ")
    rows = cursor.fetchall()
    return rows

def vol_passager(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT v.numero_vol, p.nom as nom_passager, p.prenom as prenom_passager FROM Vols v LEFT JOIN Passagers p ON v.id_vol = p.id_vol")
    rows = cursor.fetchall()
    for row in rows:
        if row[1] is None and row[2] is None:
           print(f"Vol {row[0]} : Aucun Passager")
        else:
            nom_passager = row[1] if row[1] is not None else ""
            prenom_passager = row[2] if row[2] is not None else ""
            print(f"Vol {row[0]} : {nom_passager} {prenom_passager}")