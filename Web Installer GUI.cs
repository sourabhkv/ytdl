using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Enabled = false;
            using (WebClient wc = new WebClient())
            {
                wc.DownloadProgressChanged += wc_DownloadProgressChanged;
                wc.DownloadFileAsync(
                    // Param1 = Link of file
                    new System.Uri("https://github.com/sourabhkv/ytdl/releases/latest/download/YouTube-dl.GUI.exe"),
                    // Param2 = Path to save
                    "Youtube-dl GUI.exe"
                );
            }
        }
        void wc_DownloadProgressChanged(object sender, DownloadProgressChangedEventArgs e)
        {
            progressBar1.Value = e.ProgressPercentage;
            label5.Text = (e.TotalBytesToReceive/(1024*1024)).ToString()+" MiB";
            label3.Text = (e.BytesReceived / (1024*1024)).ToString() + " Mib";
            string c = "no";
            //label2.Text = e.ProgressPercentage;
            if (progressBar1.Value == 100 & (c=="no")){
                c = "yes";
                Process.Start("Youtube-dl GUI.exe");
                Application.Exit();
            } 
        }
    }
}