

def get_count_header(header):
    """
    Reads a  header (special BCALM2 header format) and returns a count (float)
    :param header: a headers of a BCALM fasta file, containing a count
    :return: A float
    """
    kc_value = None
    header_parts = header.strip().split()
    for part in header_parts:
        if part.startswith('km:f:'):
            kc_value = float(part.split(':')[2])
            break
    
    return kc_value
#todo transformer cette fonction pour qu'elle soit directement intégrée avec l'extraction de kmers