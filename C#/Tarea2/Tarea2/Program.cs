using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tarea2
{
    class Program
    {
        static void Main(string[] args)
        {
            entrada inn = new entradaConsola();
            salida exit = new salidaConsola();

            exit.ver("Ingrese el nombre del afiliado");
            afiliado x = new afiliado();
            x.getNombre(inn.read());
            exit.ver("El empleado es " + x.setNombre());
            exit.ver("Ingrese el estado del afiliado");
            x.getEstado(inn.read());
            exit.ver(x.setNombre() + " es un afiliado " + x.setEstado());

            Console.ReadKey();
        }
    }

    public abstract class entrada
    {
        public abstract String read();
    }

    public abstract class salida
    {
        public abstract void ver(String msn);
    }

    public class entradaConsola : entrada
    {
        public override string read()
        {
            return Console.ReadLine();
        }
    }

    public class salidaConsola : salida
    {
        public override void ver(string msn)
        {
            Console.WriteLine(msn);
        }
    }

    public class afiliado
    {
        private String nombre;
        private String estado;

        public void getNombre(String nom)
        {
            this.nombre = nom;
        }

        public String setNombre()
        {
            return this.nombre;
        }

        public void getEstado(String s)
        {
            this.estado = s;
        }

        public String setEstado()
        {
            return estado;
        }
    }
}
