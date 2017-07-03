#!/usr/bin/python2

import cgi,commands

import header

if(os.environ['REQUEST_METHOD'] == "POST"):
		psss

elif(os.environ['REQUEST_METHOD'] == "GET"):

	print """

    <div class="form-photo">
        <div class="form-container">
            <div class="image-holder" style="background-image:url(&quot;/img/iaas_form.jpg&quot;);margin:5px;padding:10px;width:500px;height:599px;"></div>
            <form method="post" style="height:624px;padding-top:30px;padding-bottom:30px;padding-right:25px;padding-left:25px;">
                <h2 class="text-center" style="font-family:Quicksand, sans-serif;font-size:24px;">IAAS </h2>
                <input class="form-control" type="text" name="OSName" placeholder="OS Name/Alias">
                <div class="form-group"></div>
                <input class="form-control" type="number" name="CPUCores" placeholder="CPU Cores" min="1" max="16" step="1">
                <div class="form-group"></div>
                <div class="row">
                    <div class="clearfix"></div>
                </div>
                <div class="form-group"></div>
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr></tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <input type="range" style="height:40px;width:130px" min="512" step="512" max="16384" for="osRAMsize" name="osRAM" oninput="osRAMsize.value=osRAM.value" />
                                </td>
                                <td>
                                    <input style="width:110px" type="number" placeholder="RAM Size" class="form-control" min="512" step="512" max="16384" for="osRAM" name="osRAMsize" oninput="osRAM.value=osRAMsize.val" />
                                </td>
                                <td>
                                    <span class="input-group-addon"style="height:40px">MB</span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <input type="range" style="height:40px;width:130px" min="8" step="1" max="2048" for="osDRIVEsize" name="osDRIVE" oninput="osDRIVEsize.value=osDRIVE.value" />
                                </td>
                                <td>
                                    <input style="width:110px" type="number" placeholder="Drive Size" class="form-control" min="8" step="1" max="2048" for="osDRIVE" name="osDRIVEsize" oninput="osDRIVE.value=osDRIVEsize.val" />
                                </td>
                                <td>
                                    <span class="input-group-addon" style="height:40px">GB</span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="form-group"></div>
                <select class="form-control" value="1">
                    <option value="1">RHEL7</option>
                    <option value="2">Ubuntu 16.04</option>
                    <option value="3">Fedora Workstation</option>
                    <option value="4">Arch Linux</option>
                </select>
                <div class="form-group"></div>
                <div class="form-group"></div>
                <div class="form-group has-success">
                    <div class="checkbox">
                        <label class="control-label" style="margin:auto;">
                            <input type="checkbox"> Confirm?</label>
                    </div>
                </div>
                <div class="form-group">
                    <button class="btn btn-primary btn-block" type="submit">SUBMIT </button>
                </div>
            </form>
        </div>
    </div>
    <script src="/js/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
</body>

</html>

	"""
